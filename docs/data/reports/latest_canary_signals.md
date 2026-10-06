# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T00:22:28.052431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `-0.0589` n `235`; crypto_major avg `0.1181` n `8`; equity avg `0.0576` n `144`; fx avg `-0.0407` n `6`; index avg `0.0217` n `26`; metal avg `0.0545` n `20`; unknown avg `-0.0376` n `1079`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `0.0435` n `235`; crypto_major avg `0.049` n `8`; equity avg `-0.015` n `144`; fx avg `-0.0126` n `6`; index avg `-0.0195` n `26`; metal avg `0.0222` n `20`; unknown avg `-0.0275` n `1071`
- 4h: commodity avg `-0.0089` n `13`; crypto_alt avg `0.2409` n `235`; crypto_major avg `0.2234` n `8`; equity avg `0.1004` n `144`; fx avg `-0.0042` n `6`; index avg `0.0019` n `26`; metal avg `0.0241` n `20`; unknown avg `-0.1324` n `1019`
- 24h: commodity avg `-0.1555` n `13`; crypto_alt avg `0.2507` n `235`; crypto_major avg `0.1667` n `8`; equity avg `0.0938` n `144`; fx avg `-0.0914` n `6`; index avg `0.0856` n `26`; metal avg `0.0453` n `20`; unknown avg `625.6201` n `800`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
