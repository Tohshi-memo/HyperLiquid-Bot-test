# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T02:37:29.150412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0404` n `12`; crypto_alt avg `0.0518` n `228`; crypto_major avg `0.0236` n `8`; equity avg `0.0353` n `86`; fx avg `0.0046` n `6`; index avg `0.0021` n `23`; metal avg `-0.0284` n `20`; unknown avg `0.0231` n `764`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `0.1118` n `228`; crypto_major avg `0.0834` n `8`; equity avg `-0.1074` n `86`; fx avg `0.0099` n `6`; index avg `0.0143` n `23`; metal avg `0.0616` n `20`; unknown avg `0.3721` n `748`
- 4h: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.0163` n `228`; crypto_major avg `0.123` n `8`; equity avg `-0.5117` n `86`; fx avg `0.0983` n `6`; index avg `-0.0586` n `23`; metal avg `-0.3218` n `20`; unknown avg `-0.0273` n `732`
- 24h: commodity avg `-0.4569` n `12`; crypto_alt avg `-2.1155` n `228`; crypto_major avg `-1.8441` n `8`; equity avg `-0.3865` n `86`; fx avg `0.0905` n `6`; index avg `0.4953` n `23`; metal avg `-1.5811` n `20`; unknown avg `-0.4895` n `700`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
