# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T09:37:32.695648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0619` n `13`; crypto_alt avg `0.4795` n `235`; crypto_major avg `0.2547` n `8`; equity avg `0.1344` n `150`; fx avg `-0.0028` n `6`; index avg `0.0257` n `26`; metal avg `-0.0041` n `20`; unknown avg `1.5829` n `1077`
- 1h: commodity avg `-0.0413` n `13`; crypto_alt avg `0.7834` n `235`; crypto_major avg `0.4273` n `8`; equity avg `0.0849` n `150`; fx avg `0.0364` n `6`; index avg `0.0001` n `26`; metal avg `-0.0331` n `20`; unknown avg `0.2847` n `1075`
- 4h: commodity avg `0.3499` n `13`; crypto_alt avg `0.3811` n `235`; crypto_major avg `0.0257` n `8`; equity avg `-0.6578` n `150`; fx avg `0.0327` n `6`; index avg `-0.1476` n `26`; metal avg `-0.1738` n `20`; unknown avg `0.8478` n `1031`
- 24h: commodity avg `0.7543` n `13`; crypto_alt avg `0.5653` n `235`; crypto_major avg `-1.406` n `8`; equity avg `-1.3208` n `150`; fx avg `0.0234` n `6`; index avg `-0.2589` n `26`; metal avg `-0.0516` n `20`; unknown avg `416.5421` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
