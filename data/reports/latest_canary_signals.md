# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T01:22:29.179129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0321` n `13`; crypto_alt avg `-0.3851` n `235`; crypto_major avg `-0.3648` n `8`; equity avg `-0.0453` n `150`; fx avg `0.0074` n `6`; index avg `0.0121` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.4338` n `1077`
- 1h: commodity avg `0.1092` n `13`; crypto_alt avg `0.0128` n `235`; crypto_major avg `-0.0202` n `8`; equity avg `-0.1171` n `150`; fx avg `0.0158` n `6`; index avg `-0.0375` n `26`; metal avg `0.287` n `20`; unknown avg `1.4816` n `1075`
- 4h: commodity avg `0.2082` n `13`; crypto_alt avg `0.8895` n `235`; crypto_major avg `0.1905` n `8`; equity avg `0.0226` n `150`; fx avg `-0.0514` n `6`; index avg `-0.0345` n `26`; metal avg `0.2546` n `20`; unknown avg `0.0026` n `1069`
- 24h: commodity avg `0.3549` n `13`; crypto_alt avg `-2.9753` n `235`; crypto_major avg `-2.9537` n `8`; equity avg `-1.3211` n `150`; fx avg `-0.1876` n `6`; index avg `-0.2481` n `26`; metal avg `-0.3563` n `20`; unknown avg `248.0826` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
