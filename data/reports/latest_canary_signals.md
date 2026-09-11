# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T11:22:32.092729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0745` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.031` n `12`; crypto_alt avg `0.1722` n `233`; crypto_major avg `0.0567` n `8`; equity avg `-0.0065` n `136`; fx avg `0.0206` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.0896` n `796`
- 1h: commodity avg `0.0538` n `12`; crypto_alt avg `-0.8874` n `233`; crypto_major avg `-0.6055` n `8`; equity avg `-0.2477` n `136`; fx avg `-0.0214` n `6`; index avg `-0.0322` n `26`; metal avg `-0.1062` n `20`; unknown avg `-0.0543` n `794`
- 4h: commodity avg `-0.3188` n `12`; crypto_alt avg `-1.7637` n `233`; crypto_major avg `-1.0519` n `8`; equity avg `-0.0665` n `136`; fx avg `-0.1002` n `6`; index avg `0.0226` n `26`; metal avg `-0.0626` n `20`; unknown avg `-0.4697` n `788`
- 24h: commodity avg `0.2719` n `12`; crypto_alt avg `-2.477` n `233`; crypto_major avg `-2.1095` n `8`; equity avg `-0.931` n `136`; fx avg `-0.0993` n `6`; index avg `-0.0946` n `26`; metal avg `-0.4276` n `20`; unknown avg `0.6431` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
