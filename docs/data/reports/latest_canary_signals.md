# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T23:52:25.259051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.0585` n `230`; crypto_major avg `0.0848` n `8`; equity avg `0.0513` n `92`; fx avg `0.0243` n `6`; index avg `0.0433` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.009` n `768`
- 1h: commodity avg `-0.0422` n `12`; crypto_alt avg `0.0673` n `230`; crypto_major avg `0.0594` n `8`; equity avg `0.3696` n `92`; fx avg `-0.0113` n `6`; index avg `0.1018` n `25`; metal avg `0.0501` n `20`; unknown avg `0.0728` n `766`
- 4h: commodity avg `-0.0177` n `12`; crypto_alt avg `0.3179` n `230`; crypto_major avg `0.299` n `8`; equity avg `0.4415` n `92`; fx avg `-0.0037` n `6`; index avg `0.089` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.2147` n `766`
- 24h: commodity avg `0.0417` n `12`; crypto_alt avg `2.2678` n `230`; crypto_major avg `3.5595` n `8`; equity avg `2.4098` n `92`; fx avg `-0.0149` n `6`; index avg `0.6234` n `25`; metal avg `0.6172` n `20`; unknown avg `0.2966` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
