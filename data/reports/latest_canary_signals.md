# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T19:22:26.822497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0391` n `12`; crypto_alt avg `-0.166` n `230`; crypto_major avg `-0.2079` n `8`; equity avg `-0.2068` n `94`; fx avg `0.0029` n `6`; index avg `-0.0302` n `25`; metal avg `-0.0123` n `20`; unknown avg `-0.0441` n `768`
- 1h: commodity avg `0.1387` n `12`; crypto_alt avg `-0.4748` n `230`; crypto_major avg `-0.7412` n `8`; equity avg `-0.5531` n `94`; fx avg `-0.0007` n `6`; index avg `-0.0762` n `25`; metal avg `0.0051` n `20`; unknown avg `0.1313` n `768`
- 4h: commodity avg `0.277` n `12`; crypto_alt avg `-0.462` n `230`; crypto_major avg `-0.6386` n `8`; equity avg `0.0316` n `94`; fx avg `0.0559` n `6`; index avg `0.1046` n `25`; metal avg `0.3367` n `20`; unknown avg `-0.0777` n `768`
- 24h: commodity avg `0.1037` n `12`; crypto_alt avg `0.2` n `230`; crypto_major avg `0.3502` n `8`; equity avg `-0.8019` n `93`; fx avg `0.2139` n `6`; index avg `-0.1861` n `25`; metal avg `0.1639` n `20`; unknown avg `0.205` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
