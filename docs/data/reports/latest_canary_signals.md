# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T03:52:35.747464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1342` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8994` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7606` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5035` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0371` n `13`; crypto_alt avg `0.0588` n `235`; crypto_major avg `0.0448` n `8`; equity avg `0.068` n `150`; fx avg `0.0002` n `6`; index avg `0.0057` n `26`; metal avg `0.0297` n `20`; unknown avg `2.3494` n `1076`
- 1h: commodity avg `0.0522` n `13`; crypto_alt avg `0.0729` n `235`; crypto_major avg `0.1969` n `8`; equity avg `0.1182` n `150`; fx avg `-0.003` n `6`; index avg `0.0053` n `26`; metal avg `0.0075` n `20`; unknown avg `2.1621` n `1074`
- 4h: commodity avg `0.1999` n `13`; crypto_alt avg `-2.8049` n `235`; crypto_major avg `-1.9343` n `8`; equity avg `-0.4308` n `150`; fx avg `-0.0341` n `6`; index avg `-0.0349` n `26`; metal avg `-0.1737` n `20`; unknown avg `2.0835` n `1068`
- 24h: commodity avg `0.4875` n `13`; crypto_alt avg `-2.5826` n `235`; crypto_major avg `-2.1444` n `8`; equity avg `0.0627` n `149`; fx avg `0.064` n `6`; index avg `0.0001` n `26`; metal avg `-0.0395` n `20`; unknown avg `871.4105` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
