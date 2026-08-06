# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T09:52:25.680159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0371` n `12`; crypto_alt avg `-0.0762` n `230`; crypto_major avg `-0.1578` n `8`; equity avg `0.0977` n `108`; fx avg `-0.0112` n `6`; index avg `0.0099` n `25`; metal avg `-0.0257` n `20`; unknown avg `20.3386` n `782`
- 1h: commodity avg `0.0884` n `12`; crypto_alt avg `-0.4096` n `230`; crypto_major avg `-0.6395` n `8`; equity avg `-0.0745` n `108`; fx avg `-0.0107` n `6`; index avg `-0.0171` n `25`; metal avg `0.047` n `20`; unknown avg `20.2006` n `782`
- 4h: commodity avg `0.1241` n `12`; crypto_alt avg `-0.1692` n `230`; crypto_major avg `-0.6803` n `8`; equity avg `-0.1721` n `108`; fx avg `0.0699` n `6`; index avg `-0.013` n `25`; metal avg `0.1021` n `20`; unknown avg `21.1816` n `750`
- 24h: commodity avg `-0.2663` n `12`; crypto_alt avg `-0.0891` n `230`; crypto_major avg `-0.6564` n `8`; equity avg `-1.5576` n `108`; fx avg `-0.0104` n `6`; index avg `-0.315` n `25`; metal avg `0.5255` n `20`; unknown avg `21.3399` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
