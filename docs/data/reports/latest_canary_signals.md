# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T20:15:22.370439+00:00`
- Correlation status: `ready`
- Asset price records: `104`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `7`; crypto_alt avg `0.0037` n `223`; crypto_major avg `-0.0495` n `7`; equity avg `0.0456` n `42`; fx avg `0.0` n `4`; index avg `-0.0008` n `9`; metal avg `-0.0076` n `7`; unknown avg `0.4292` n `313`
- 1h: commodity avg `-0.0123` n `7`; crypto_alt avg `0.1293` n `223`; crypto_major avg `-0.1539` n `7`; equity avg `0.0913` n `42`; fx avg `0.0074` n `4`; index avg `0.0042` n `9`; metal avg `0.0013` n `7`; unknown avg `0.3643` n `313`
- 4h: commodity avg `-0.1736` n `7`; crypto_alt avg `0.4148` n `223`; crypto_major avg `-0.0663` n `7`; equity avg `0.2921` n `42`; fx avg `0.0412` n `4`; index avg `0.0455` n `9`; metal avg `-0.0441` n `7`; unknown avg `0.5387` n `313`
- 24h: commodity avg `-0.0186` n `7`; crypto_alt avg `1.642` n `223`; crypto_major avg `0.2036` n `7`; equity avg `0.9268` n `42`; fx avg `-0.0202` n `4`; index avg `0.061` n `9`; metal avg `-0.1007` n `7`; unknown avg `0.5875` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.525`, n `96`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5077`, n `100`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5074`, n `96`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4901`, n `100`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4456`, n `96`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4279`, n `96`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4244`, n `96`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.424`, n `100`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4179`, n `96`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4167`, n `96`, moderate_sample_signal
