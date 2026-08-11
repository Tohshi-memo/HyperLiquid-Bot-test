# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T15:44:46.685529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0408` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1194` n `12`; crypto_alt avg `-0.7984` n `230`; crypto_major avg `-0.4597` n `8`; equity avg `-0.1868` n `113`; fx avg `0.0049` n `6`; index avg `-0.0368` n `25`; metal avg `-0.0894` n `20`; unknown avg `-0.1567` n `785`
- 1h: commodity avg `0.1192` n `12`; crypto_alt avg `-1.2961` n `230`; crypto_major avg `-0.621` n `8`; equity avg `-0.0824` n `113`; fx avg `0.0057` n `6`; index avg `-0.0467` n `25`; metal avg `-0.1391` n `20`; unknown avg `-0.1608` n `785`
- 4h: commodity avg `0.19` n `12`; crypto_alt avg `-1.611` n `230`; crypto_major avg `-1.0742` n `8`; equity avg `0.1834` n `113`; fx avg `0.0171` n `6`; index avg `-0.0334` n `25`; metal avg `-0.2202` n `20`; unknown avg `0.1073` n `785`
- 24h: commodity avg `0.2084` n `12`; crypto_alt avg `-2.2304` n `230`; crypto_major avg `-0.5727` n `8`; equity avg `0.208` n `113`; fx avg `-0.0472` n `6`; index avg `0.1078` n `25`; metal avg `0.0645` n `20`; unknown avg `-0.319` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1977`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
