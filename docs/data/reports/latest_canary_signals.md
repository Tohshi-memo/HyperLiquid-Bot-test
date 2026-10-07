# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T11:52:27.814003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2308` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0235` n `13`; crypto_alt avg `-0.1523` n `235`; crypto_major avg `-0.072` n `8`; equity avg `-0.0916` n `150`; fx avg `-0.006` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0357` n `20`; unknown avg `0.5167` n `1076`
- 1h: commodity avg `0.0777` n `13`; crypto_alt avg `-0.6492` n `235`; crypto_major avg `-0.3614` n `8`; equity avg `-0.3473` n `150`; fx avg `-0.018` n `6`; index avg `-0.0601` n `26`; metal avg `-0.0233` n `20`; unknown avg `1.7101` n `1074`
- 4h: commodity avg `0.1549` n `13`; crypto_alt avg `-1.9964` n `235`; crypto_major avg `-1.3835` n `8`; equity avg `-0.9672` n `150`; fx avg `-0.0443` n `6`; index avg `-0.1527` n `26`; metal avg `-0.2449` n `20`; unknown avg `1.5619` n `1058`
- 24h: commodity avg `1.4014` n `13`; crypto_alt avg `-5.55` n `235`; crypto_major avg `-3.8436` n `8`; equity avg `-1.7519` n `150`; fx avg `-0.1713` n `6`; index avg `-0.4055` n `26`; metal avg `-0.6136` n `20`; unknown avg `816.0092` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
