# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T21:07:23.825472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `0.5425` n `231`; crypto_major avg `0.5227` n `8`; equity avg `0.0133` n `122`; fx avg `-0.0015` n `6`; index avg `0.0003` n `25`; metal avg `0.0049` n `20`; unknown avg `0.462` n `793`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `0.6998` n `231`; crypto_major avg `0.7107` n `8`; equity avg `0.0212` n `122`; fx avg `-0.0367` n `6`; index avg `-0.0045` n `25`; metal avg `0.0422` n `20`; unknown avg `0.5259` n `793`
- 4h: commodity avg `-0.0716` n `12`; crypto_alt avg `0.592` n `231`; crypto_major avg `0.4323` n `8`; equity avg `0.219` n `122`; fx avg `-0.0757` n `6`; index avg `0.0336` n `25`; metal avg `0.0439` n `20`; unknown avg `1.5132` n `793`
- 24h: commodity avg `-0.1149` n `12`; crypto_alt avg `3.5511` n `231`; crypto_major avg `1.2008` n `8`; equity avg `0.7811` n `122`; fx avg `-0.0719` n `6`; index avg `0.1291` n `25`; metal avg `0.123` n `20`; unknown avg `6.6392` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
