# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T23:07:26.611510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2221` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.8827` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8609` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.0503` n `231`; crypto_major avg `-0.0818` n `8`; equity avg `-0.1718` n `128`; fx avg `0.0059` n `6`; index avg `-0.0202` n `26`; metal avg `0.0537` n `20`; unknown avg `-0.1225` n `791`
- 1h: commodity avg `-0.1936` n `12`; crypto_alt avg `-0.9103` n `231`; crypto_major avg `-0.8538` n `8`; equity avg `-0.3367` n `128`; fx avg `0.0192` n `6`; index avg `-0.0302` n `26`; metal avg `0.1617` n `20`; unknown avg `1.0724` n `791`
- 4h: commodity avg `0.2172` n `12`; crypto_alt avg `-1.6001` n `231`; crypto_major avg `-2.0049` n `8`; equity avg `-0.6216` n `128`; fx avg `0.0065` n `6`; index avg `-0.144` n `26`; metal avg `-0.1222` n `20`; unknown avg `0.9722` n `791`
- 24h: commodity avg `0.2784` n `12`; crypto_alt avg `0.2453` n `231`; crypto_major avg `-0.9363` n `8`; equity avg `-0.4421` n `128`; fx avg `0.0371` n `6`; index avg `-0.0901` n `26`; metal avg `-0.0179` n `20`; unknown avg `-0.1406` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
