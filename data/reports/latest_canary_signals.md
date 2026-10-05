# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T10:07:31.162047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `0.061` n `235`; crypto_major avg `0.0609` n `8`; equity avg `0.0489` n `144`; fx avg `0.0097` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0153` n `20`; unknown avg `44.1742` n `1077`
- 1h: commodity avg `-0.1062` n `13`; crypto_alt avg `-0.0781` n `235`; crypto_major avg `-0.1803` n `8`; equity avg `-0.0935` n `144`; fx avg `0.0064` n `6`; index avg `-0.0268` n `26`; metal avg `-0.102` n `20`; unknown avg `44.4279` n `1077`
- 4h: commodity avg `0.2294` n `13`; crypto_alt avg `0.3802` n `235`; crypto_major avg `0.3622` n `8`; equity avg `-0.1309` n `144`; fx avg `0.0521` n `6`; index avg `-0.0379` n `26`; metal avg `0.1152` n `20`; unknown avg `6.2907` n `997`
- 24h: commodity avg `-0.1167` n `13`; crypto_alt avg `0.8712` n `235`; crypto_major avg `0.9037` n `8`; equity avg `0.1251` n `144`; fx avg `-0.0386` n `6`; index avg `-0.0875` n `26`; metal avg `0.2449` n `20`; unknown avg `0.7089` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2076`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
