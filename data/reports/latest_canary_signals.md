# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T02:07:29.779364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6853` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.407` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.3225` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.2866` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.2524` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.2002` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7168` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.5709` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.035` n `13`; crypto_alt avg `-2.4909` n `235`; crypto_major avg `-1.9292` n `8`; equity avg `-0.4835` n `150`; fx avg `-0.0107` n `6`; index avg `-0.0538` n `26`; metal avg `-0.0921` n `20`; unknown avg `1.8553` n `1074`
- 1h: commodity avg `-0.017` n `13`; crypto_alt avg `-3.1751` n `235`; crypto_major avg `-2.3395` n `8`; equity avg `-0.7686` n `150`; fx avg `-0.0123` n `6`; index avg `-0.0871` n `26`; metal avg `-0.1393` n `20`; unknown avg `2.1794` n `1074`
- 4h: commodity avg `0.195` n `13`; crypto_alt avg `-3.3814` n `235`; crypto_major avg `-2.4903` n `8`; equity avg `-0.7735` n `150`; fx avg `-0.0103` n `6`; index avg `-0.0833` n `26`; metal avg `-0.2037` n `20`; unknown avg `2.8056` n `1068`
- 24h: commodity avg `0.4455` n `13`; crypto_alt avg `-3.5114` n `235`; crypto_major avg `-2.8441` n `8`; equity avg `-0.2617` n `149`; fx avg `0.0673` n `6`; index avg `-0.037` n `26`; metal avg `-0.0865` n `20`; unknown avg `871.2393` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
