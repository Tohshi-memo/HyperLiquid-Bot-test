# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T04:22:34.078782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.1038` n `231`; crypto_major avg `0.0408` n `8`; equity avg `0.0396` n `122`; fx avg `-0.0103` n `6`; index avg `0.0063` n `25`; metal avg `-0.0078` n `20`; unknown avg `0.1028` n `797`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `-0.09` n `231`; crypto_major avg `-0.011` n `8`; equity avg `0.2022` n `122`; fx avg `-0.051` n `6`; index avg `0.0261` n `25`; metal avg `-0.045` n `20`; unknown avg `0.0123` n `797`
- 4h: commodity avg `-0.0808` n `12`; crypto_alt avg `1.2649` n `231`; crypto_major avg `0.9057` n `8`; equity avg `0.3151` n `122`; fx avg `-0.045` n `6`; index avg `0.1048` n `25`; metal avg `0.0927` n `20`; unknown avg `1.0477` n `796`
- 24h: commodity avg `-0.8376` n `12`; crypto_alt avg `-2.4761` n `231`; crypto_major avg `-2.4742` n `8`; equity avg `1.4141` n `122`; fx avg `-0.0153` n `6`; index avg `0.1967` n `25`; metal avg `0.2758` n `20`; unknown avg `0.4254` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
