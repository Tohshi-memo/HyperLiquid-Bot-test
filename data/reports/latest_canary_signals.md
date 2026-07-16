# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T21:22:31.934860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `12`; crypto_alt avg `0.0235` n `230`; crypto_major avg `-0.0226` n `8`; equity avg `0.0079` n `94`; fx avg `-0.0008` n `6`; index avg `0.004` n `25`; metal avg `0.0113` n `20`; unknown avg `0.0064` n `768`
- 1h: commodity avg `0.1095` n `12`; crypto_alt avg `0.1136` n `230`; crypto_major avg `0.0261` n `8`; equity avg `0.0539` n `94`; fx avg `0.0031` n `6`; index avg `0.0283` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.0297` n `768`
- 4h: commodity avg `0.2265` n `12`; crypto_alt avg `0.0123` n `230`; crypto_major avg `-0.0751` n `8`; equity avg `-0.342` n `94`; fx avg `-0.0099` n `6`; index avg `-0.023` n `25`; metal avg `-0.1351` n `20`; unknown avg `-0.0426` n `768`
- 24h: commodity avg `-0.1826` n `12`; crypto_alt avg `-0.9569` n `230`; crypto_major avg `-2.0565` n `8`; equity avg `-3.726` n `94`; fx avg `-0.1699` n `6`; index avg `-0.5006` n `25`; metal avg `-0.8314` n `20`; unknown avg `-0.3852` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
