# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T03:22:17.513373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0382` n `12`; crypto_alt avg `0.2015` n `228`; crypto_major avg `0.0691` n `8`; equity avg `-0.0283` n `67`; fx avg `-0.0022` n `6`; index avg `-0.0031` n `23`; metal avg `0.0197` n `18`; unknown avg `0.0334` n `386`
- 1h: commodity avg `-0.1973` n `12`; crypto_alt avg `0.4028` n `228`; crypto_major avg `0.349` n `8`; equity avg `0.0782` n `67`; fx avg `0.0003` n `6`; index avg `0.0451` n `23`; metal avg `0.066` n `18`; unknown avg `-0.1422` n `386`
- 4h: commodity avg `0.099` n `12`; crypto_alt avg `0.1359` n `228`; crypto_major avg `-0.1321` n `8`; equity avg `-0.2485` n `67`; fx avg `-0.0078` n `6`; index avg `-0.0326` n `23`; metal avg `-0.0572` n `18`; unknown avg `-1.021` n `386`
- 24h: commodity avg `-0.0235` n `12`; crypto_alt avg `-3.223` n `228`; crypto_major avg `-2.4842` n `8`; equity avg `-1.6528` n `67`; fx avg `0.0727` n `6`; index avg `0.0777` n `23`; metal avg `-0.5407` n `18`; unknown avg `-2.0876` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
