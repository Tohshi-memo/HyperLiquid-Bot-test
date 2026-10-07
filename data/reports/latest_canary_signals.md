# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T05:22:27.759166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5788` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0314` n `13`; crypto_alt avg `0.1394` n `235`; crypto_major avg `0.0992` n `8`; equity avg `-0.0827` n `150`; fx avg `0.0025` n `6`; index avg `-0.0126` n `26`; metal avg `-0.038` n `20`; unknown avg `0.4006` n `1076`
- 1h: commodity avg `0.0481` n `13`; crypto_alt avg `0.15` n `235`; crypto_major avg `0.2197` n `8`; equity avg `-0.1457` n `150`; fx avg `-0.0057` n `6`; index avg `-0.0222` n `26`; metal avg `-0.0908` n `20`; unknown avg `0.3265` n `1074`
- 4h: commodity avg `0.0865` n `13`; crypto_alt avg `-2.8537` n `235`; crypto_major avg `-1.6479` n `8`; equity avg `-0.5423` n `150`; fx avg `-0.025` n `6`; index avg `-0.0691` n `26`; metal avg `-0.1876` n `20`; unknown avg `1.868` n `1068`
- 24h: commodity avg `0.4913` n `13`; crypto_alt avg `-3.3105` n `235`; crypto_major avg `-2.3066` n `8`; equity avg `-0.1424` n `149`; fx avg `0.0441` n `6`; index avg `-0.0396` n `26`; metal avg `-0.0743` n `20`; unknown avg `871.654` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
