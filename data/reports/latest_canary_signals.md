# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T15:54:17.827974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `0.0659` n `230`; crypto_major avg `0.0177` n `8`; equity avg `-0.0151` n `114`; fx avg `-0.0001` n `6`; index avg `0.0007` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0033` n `791`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `0.2382` n `230`; crypto_major avg `0.149` n `8`; equity avg `0.0193` n `114`; fx avg `-0.0007` n `6`; index avg `0.0067` n `25`; metal avg `-0.0001` n `20`; unknown avg `5.6127` n `791`
- 4h: commodity avg `-0.033` n `12`; crypto_alt avg `0.4376` n `230`; crypto_major avg `0.2845` n `8`; equity avg `0.042` n `114`; fx avg `-0.0055` n `6`; index avg `0.0235` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.0331` n `791`
- 24h: commodity avg `-0.0819` n `12`; crypto_alt avg `1.2988` n `230`; crypto_major avg `0.3432` n `8`; equity avg `0.4416` n `114`; fx avg `0.0211` n `6`; index avg `0.0624` n `25`; metal avg `-0.0144` n `20`; unknown avg `-0.0506` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
