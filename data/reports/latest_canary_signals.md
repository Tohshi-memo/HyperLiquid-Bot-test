# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T18:45:24.131016+00:00`
- Correlation status: `ready`
- Asset price records: `98`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `7`; crypto_alt avg `-0.0027` n `223`; crypto_major avg `-0.0693` n `7`; equity avg `-0.0693` n `42`; fx avg `0.0` n `4`; index avg `0.002` n `9`; metal avg `0.0112` n `7`; unknown avg `-0.0078` n `313`
- 1h: commodity avg `-0.0222` n `7`; crypto_alt avg `0.125` n `223`; crypto_major avg `0.0137` n `7`; equity avg `0.0617` n `42`; fx avg `0.0011` n `4`; index avg `0.0213` n `9`; metal avg `-0.0085` n `7`; unknown avg `0.0394` n `313`
- 4h: commodity avg `-0.1609` n `7`; crypto_alt avg `0.6883` n `223`; crypto_major avg `0.0782` n `7`; equity avg `0.1604` n `42`; fx avg `0.0818` n `4`; index avg `0.0337` n `9`; metal avg `-0.0102` n `7`; unknown avg `-0.0506` n `313`
- 24h: commodity avg `0.0405` n `7`; crypto_alt avg `1.2874` n `223`; crypto_major avg `0.1232` n `7`; equity avg `0.6773` n `42`; fx avg `-0.0287` n `4`; index avg `0.0852` n `9`; metal avg `-0.2671` n `7`; unknown avg `0.4006` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5331`, n `90`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5236`, n `94`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5065`, n `90`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5054`, n `94`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4672`, n `90`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4326`, n `90`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4264`, n `90`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4244`, n `94`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.423`, n `90`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4219`, n `90`, moderate_sample_signal
