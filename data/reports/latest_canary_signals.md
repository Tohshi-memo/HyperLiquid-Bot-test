# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T02:30:09.271275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `13`; crypto_alt avg `-0.0341` n `235`; crypto_major avg `-0.0073` n `8`; equity avg `-0.4621` n `151`; fx avg `-0.0068` n `6`; index avg `0.0193` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.001` n `1113`
- 1h: commodity avg `-0.0893` n `13`; crypto_alt avg `0.3922` n `235`; crypto_major avg `0.28` n `8`; equity avg `-0.406` n `151`; fx avg `-0.0268` n `6`; index avg `0.0416` n `26`; metal avg `0.0883` n `20`; unknown avg `0.7252` n `1111`
- 4h: commodity avg `-0.5903` n `13`; crypto_alt avg `0.0889` n `235`; crypto_major avg `0.3364` n `8`; equity avg `-0.4724` n `151`; fx avg `-0.0521` n `6`; index avg `-0.0004` n `26`; metal avg `0.1941` n `20`; unknown avg `2.4828` n `1089`
- 24h: commodity avg `-0.4172` n `13`; crypto_alt avg `1.6233` n `235`; crypto_major avg `0.9712` n `8`; equity avg `-0.1632` n `151`; fx avg `-0.0542` n `6`; index avg `0.0403` n `26`; metal avg `0.2213` n `20`; unknown avg `0.7732` n `928`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
