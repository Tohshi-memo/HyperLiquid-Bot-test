# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T06:37:24.539366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2749` n `13`; crypto_alt avg `0.0276` n `235`; crypto_major avg `-0.0335` n `8`; equity avg `-0.1407` n `150`; fx avg `0.006` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0339` n `20`; unknown avg `-0.0246` n `1077`
- 1h: commodity avg `0.2617` n `13`; crypto_alt avg `-0.7029` n `235`; crypto_major avg `-0.477` n `8`; equity avg `-0.6037` n `150`; fx avg `-0.0239` n `6`; index avg `-0.1326` n `26`; metal avg `-0.1718` n `20`; unknown avg `0.2489` n `1047`
- 4h: commodity avg `0.3659` n `13`; crypto_alt avg `-1.1394` n `235`; crypto_major avg `-1.1056` n `8`; equity avg `-1.0565` n `150`; fx avg `-0.0202` n `6`; index avg `-0.1903` n `26`; metal avg `-0.2918` n `20`; unknown avg `1.4237` n `1041`
- 24h: commodity avg `0.6809` n `13`; crypto_alt avg `-1.5193` n `235`; crypto_major avg `-2.6764` n `8`; equity avg `-1.8527` n `150`; fx avg `-0.1485` n `6`; index avg `-0.3161` n `26`; metal avg `-0.2724` n `20`; unknown avg `416.8857` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
