# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T10:22:26.259574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.0047` n `230`; crypto_major avg `0.1341` n `8`; equity avg `0.0401` n `112`; fx avg `0.0` n `6`; index avg `0.0105` n `25`; metal avg `0.0151` n `20`; unknown avg `-0.0033` n `785`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `0.0521` n `230`; crypto_major avg `0.2642` n `8`; equity avg `0.0118` n `112`; fx avg `-0.0016` n `6`; index avg `-0.0013` n `25`; metal avg `0.0057` n `20`; unknown avg `0.0199` n `785`
- 4h: commodity avg `0.0422` n `12`; crypto_alt avg `-0.059` n `230`; crypto_major avg `0.1636` n `8`; equity avg `-0.0715` n `112`; fx avg `0.0076` n `6`; index avg `0.0049` n `25`; metal avg `0.0131` n `20`; unknown avg `-0.0387` n `785`
- 24h: commodity avg `0.2676` n `12`; crypto_alt avg `1.1627` n `230`; crypto_major avg `0.435` n `8`; equity avg `0.462` n `112`; fx avg `-0.0212` n `6`; index avg `0.0574` n `25`; metal avg `0.0063` n `20`; unknown avg `0.1784` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0438`, n `668`, weak_sample_signal
