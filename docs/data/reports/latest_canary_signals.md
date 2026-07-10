# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T13:22:30.788652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0331` n `12`; crypto_alt avg `-0.0178` n `229`; crypto_major avg `0.0229` n `8`; equity avg `0.0301` n `91`; fx avg `-0.0118` n `6`; index avg `0.0038` n `25`; metal avg `-0.0359` n `20`; unknown avg `0.0237` n `766`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.1203` n `229`; crypto_major avg `-0.273` n `8`; equity avg `-0.1305` n `91`; fx avg `-0.0303` n `6`; index avg `-0.0356` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.1069` n `766`
- 4h: commodity avg `0.0244` n `12`; crypto_alt avg `0.1275` n `229`; crypto_major avg `-0.1865` n `8`; equity avg `0.3216` n `91`; fx avg `-0.0235` n `6`; index avg `-0.0041` n `25`; metal avg `0.0269` n `20`; unknown avg `-0.0714` n `766`
- 24h: commodity avg `-0.7927` n `12`; crypto_alt avg `1.1224` n `229`; crypto_major avg `1.5678` n `8`; equity avg `0.0927` n `91`; fx avg `-0.1223` n `6`; index avg `0.0478` n `25`; metal avg `-0.0898` n `20`; unknown avg `-0.0619` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
