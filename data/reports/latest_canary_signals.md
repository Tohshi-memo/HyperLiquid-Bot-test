# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T18:22:30.346194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2279` n `13`; crypto_alt avg `-0.0793` n `235`; crypto_major avg `-0.2083` n `8`; equity avg `-0.0301` n `150`; fx avg `0.0043` n `6`; index avg `-0.0073` n `26`; metal avg `-0.031` n `20`; unknown avg `0.3685` n `1077`
- 1h: commodity avg `0.0699` n `13`; crypto_alt avg `-0.0148` n `235`; crypto_major avg `-0.3885` n `8`; equity avg `-0.051` n `150`; fx avg `0.0061` n `6`; index avg `-0.0188` n `26`; metal avg `-0.088` n `20`; unknown avg `-0.0683` n `1075`
- 4h: commodity avg `-0.3227` n `13`; crypto_alt avg `0.4724` n `235`; crypto_major avg `-0.2916` n `8`; equity avg `0.2123` n `150`; fx avg `-0.002` n `6`; index avg `0.1186` n `26`; metal avg `0.1115` n `20`; unknown avg `0.2233` n `1068`
- 24h: commodity avg `0.5118` n `13`; crypto_alt avg `-4.8746` n `235`; crypto_major avg `-3.8632` n `8`; equity avg `-1.5462` n `150`; fx avg `-0.1796` n `6`; index avg `-0.2544` n `26`; metal avg `-0.658` n `20`; unknown avg `15.4645` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
