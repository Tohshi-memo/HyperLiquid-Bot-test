# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T02:23:03.471774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4281` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.141` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0453` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.8484` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.8229` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0155` n `13`; crypto_alt avg `0.4345` n `235`; crypto_major avg `0.2409` n `8`; equity avg `-0.0025` n `150`; fx avg `0.0193` n `6`; index avg `-0.0121` n `26`; metal avg `0.0083` n `20`; unknown avg `0.4034` n `1076`
- 1h: commodity avg `-0.0044` n `13`; crypto_alt avg `-2.6173` n `235`; crypto_major avg `-1.9338` n `8`; equity avg `-0.6971` n `150`; fx avg `0.0162` n `6`; index avg `-0.0854` n `26`; metal avg `-0.1109` n `20`; unknown avg `1.3436` n `1074`
- 4h: commodity avg `0.1914` n `13`; crypto_alt avg `-2.8602` n `235`; crypto_major avg `-2.2367` n `8`; equity avg `-0.7873` n `150`; fx avg `0.0076` n `6`; index avg `-0.0957` n `26`; metal avg `-0.1914` n `20`; unknown avg `1.9775` n `1068`
- 24h: commodity avg `0.4625` n `13`; crypto_alt avg `-3.179` n `235`; crypto_major avg `-2.7355` n `8`; equity avg `-0.2978` n `149`; fx avg `0.0886` n `6`; index avg `-0.0493` n `26`; metal avg `-0.0737` n `20`; unknown avg `871.2274` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
