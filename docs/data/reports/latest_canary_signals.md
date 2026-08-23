# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T19:22:29.512898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.0621` n `231`; crypto_major avg `-0.0207` n `8`; equity avg `0.0438` n `122`; fx avg `0.0009` n `6`; index avg `0.0038` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.0165` n `793`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `0.0808` n `231`; crypto_major avg `-0.0858` n `8`; equity avg `0.1274` n `122`; fx avg `-0.0142` n `6`; index avg `0.018` n `25`; metal avg `0.0109` n `20`; unknown avg `0.2137` n `793`
- 4h: commodity avg `-0.0757` n `12`; crypto_alt avg `0.7197` n `231`; crypto_major avg `0.3264` n `8`; equity avg `0.2801` n `122`; fx avg `-0.0054` n `6`; index avg `0.0421` n `25`; metal avg `0.0324` n `20`; unknown avg `0.6063` n `793`
- 24h: commodity avg `-0.0287` n `12`; crypto_alt avg `2.4523` n `231`; crypto_major avg `0.6185` n `8`; equity avg `0.8462` n `122`; fx avg `0.0141` n `6`; index avg `0.1302` n `25`; metal avg `0.0885` n `20`; unknown avg `5.3247` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
