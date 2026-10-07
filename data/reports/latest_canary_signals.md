# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T03:22:29.570133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1817` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9552` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7853` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.2113` n `235`; crypto_major avg `-0.1547` n `8`; equity avg `0.0085` n `150`; fx avg `-0.0116` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0304` n `20`; unknown avg `-0.168` n `1076`
- 1h: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.108` n `235`; crypto_major avg `0.1123` n `8`; equity avg `0.2129` n `150`; fx avg `-0.0269` n `6`; index avg `0.0347` n `26`; metal avg `-0.0345` n `20`; unknown avg `1.5176` n `1074`
- 4h: commodity avg `0.1677` n `13`; crypto_alt avg `-3.0611` n `235`; crypto_major avg `-2.014` n `8`; equity avg `-0.5729` n `150`; fx avg `-0.0202` n `6`; index avg `-0.0588` n `26`; metal avg `-0.2287` n `20`; unknown avg `1.8982` n `1068`
- 24h: commodity avg `0.4384` n `13`; crypto_alt avg `-2.9544` n `235`; crypto_major avg `-2.4081` n `8`; equity avg `-0.0568` n `149`; fx avg `0.0637` n `6`; index avg `-0.005` n `26`; metal avg `-0.111` n `20`; unknown avg `871.0989` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
