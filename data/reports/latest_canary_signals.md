# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T13:37:31.690903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5752` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0601` n `13`; crypto_alt avg `-0.3436` n `235`; crypto_major avg `-0.4849` n `8`; equity avg `-0.3225` n `150`; fx avg `0.0155` n `6`; index avg `-0.0312` n `26`; metal avg `-0.0005` n `20`; unknown avg `8.3459` n `1075`
- 1h: commodity avg `-0.0499` n `13`; crypto_alt avg `-0.1732` n `235`; crypto_major avg `-0.1835` n `8`; equity avg `-0.156` n `150`; fx avg `-0.0025` n `6`; index avg `0.0199` n `26`; metal avg `-0.0376` n `20`; unknown avg `5.0464` n `1073`
- 4h: commodity avg `0.148` n `13`; crypto_alt avg `-1.4224` n `235`; crypto_major avg `-1.5959` n `8`; equity avg `-0.525` n `150`; fx avg `0.0075` n `6`; index avg `-0.0207` n `26`; metal avg `-0.1204` n `20`; unknown avg `1.9892` n `1067`
- 24h: commodity avg `0.5889` n `13`; crypto_alt avg `0.4104` n `235`; crypto_major avg `-1.9383` n `8`; equity avg `-1.0479` n `150`; fx avg `0.0482` n `6`; index avg `-0.0738` n `26`; metal avg `0.1394` n `20`; unknown avg `417.7507` n `972`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
