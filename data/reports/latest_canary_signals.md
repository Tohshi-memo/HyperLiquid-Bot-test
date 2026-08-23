# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T14:37:26.145434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.002` n `231`; crypto_major avg `-0.0078` n `8`; equity avg `-0.0093` n `122`; fx avg `0.0015` n `6`; index avg `0.0023` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0492` n `793`
- 1h: commodity avg `-0.0009` n `12`; crypto_alt avg `0.3892` n `231`; crypto_major avg `0.3236` n `8`; equity avg `0.0247` n `122`; fx avg `-0.0072` n `6`; index avg `0.0076` n `25`; metal avg `-0.02` n `20`; unknown avg `0.135` n `793`
- 4h: commodity avg `-0.0073` n `12`; crypto_alt avg `2.5462` n `231`; crypto_major avg `1.4733` n `8`; equity avg `0.2358` n `122`; fx avg `-0.02` n `6`; index avg `0.0194` n `25`; metal avg `0.0361` n `20`; unknown avg `2.7568` n `793`
- 24h: commodity avg `0.0537` n `12`; crypto_alt avg `2.4478` n `231`; crypto_major avg `2.3197` n `8`; equity avg `0.5426` n `122`; fx avg `0.045` n `6`; index avg `0.0611` n `25`; metal avg `0.0475` n `20`; unknown avg `8.7` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
