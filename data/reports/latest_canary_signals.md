# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T04:22:32.908248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1079` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9079` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8054` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.023` n `13`; crypto_alt avg `0.0468` n `235`; crypto_major avg `-0.001` n `8`; equity avg `0.0144` n `150`; fx avg `-0.0133` n `6`; index avg `-0.0008` n `26`; metal avg `0.0018` n `20`; unknown avg `0.023` n `1076`
- 1h: commodity avg `0.043` n `13`; crypto_alt avg `-0.2862` n `235`; crypto_major avg `-0.0405` n `8`; equity avg `0.0912` n `150`; fx avg `-0.0085` n `6`; index avg `0.0039` n `26`; metal avg `0.0485` n `20`; unknown avg `0.207` n `1068`
- 4h: commodity avg `0.1233` n `13`; crypto_alt avg `-3.087` n `235`; crypto_major avg `-1.9846` n `8`; equity avg `-0.607` n `150`; fx avg `-0.0676` n `6`; index avg `-0.0767` n `26`; metal avg `-0.1792` n `20`; unknown avg `1.6564` n `1068`
- 24h: commodity avg `0.5309` n `13`; crypto_alt avg `-3.3207` n `235`; crypto_major avg `-2.5256` n `8`; equity avg `0.0075` n `149`; fx avg `0.0385` n `6`; index avg `-0.0164` n `26`; metal avg `-0.0393` n `20`; unknown avg `871.2134` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
