# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T19:52:28.321678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `0.0922` n `228`; crypto_major avg `0.0955` n `8`; equity avg `-0.0539` n `86`; fx avg `0.0076` n `6`; index avg `0.0067` n `23`; metal avg `-0.0486` n `20`; unknown avg `0.1383` n `764`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.1847` n `228`; crypto_major avg `0.1017` n `8`; equity avg `0.1577` n `86`; fx avg `0.0045` n `6`; index avg `0.0339` n `23`; metal avg `0.0648` n `20`; unknown avg `0.1292` n `756`
- 4h: commodity avg `-0.0339` n `12`; crypto_alt avg `0.3127` n `228`; crypto_major avg `0.2547` n `8`; equity avg `-0.4818` n `86`; fx avg `0.0109` n `6`; index avg `-0.0692` n `23`; metal avg `-0.2277` n `20`; unknown avg `0.102` n `756`
- 24h: commodity avg `-0.4234` n `12`; crypto_alt avg `-2.9135` n `228`; crypto_major avg `-3.8239` n `8`; equity avg `-3.3962` n `86`; fx avg `-0.1863` n `6`; index avg `-0.9397` n `23`; metal avg `-1.145` n `20`; unknown avg `0.0371` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
