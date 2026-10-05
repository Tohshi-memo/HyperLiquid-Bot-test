# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T15:22:33.997259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `-0.0793` n `235`; crypto_major avg `-0.0987` n `8`; equity avg `-0.0834` n `144`; fx avg `-0.0151` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0817` n `20`; unknown avg `0.2722` n `1079`
- 1h: commodity avg `0.3491` n `13`; crypto_alt avg `-0.7501` n `235`; crypto_major avg `-0.6638` n `8`; equity avg `-0.0539` n `144`; fx avg `0.054` n `6`; index avg `-0.0259` n `26`; metal avg `-0.0968` n `20`; unknown avg `2.2059` n `1019`
- 4h: commodity avg `0.1706` n `13`; crypto_alt avg `-0.9294` n `235`; crypto_major avg `-0.6307` n `8`; equity avg `0.0693` n `144`; fx avg `-0.0363` n `6`; index avg `0.0833` n `26`; metal avg `-0.1953` n `20`; unknown avg `1.3307` n `989`
- 24h: commodity avg `-0.0514` n `13`; crypto_alt avg `-0.0946` n `235`; crypto_major avg `0.2205` n `8`; equity avg `0.1289` n `144`; fx avg `-0.089` n `6`; index avg `0.0461` n `26`; metal avg `0.0973` n `20`; unknown avg `0.0974` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
