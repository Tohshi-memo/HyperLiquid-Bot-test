# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T05:22:30.319939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.1627` n `234`; crypto_major avg `0.0651` n `8`; equity avg `-0.0046` n `141`; fx avg `0.0076` n `6`; index avg `0.001` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.2` n `961`
- 1h: commodity avg `0.0068` n `12`; crypto_alt avg `0.2422` n `234`; crypto_major avg `-0.1722` n `8`; equity avg `-0.0062` n `141`; fx avg `0.0169` n `6`; index avg `0.0052` n `26`; metal avg `-0.0072` n `20`; unknown avg `103.4135` n `959`
- 4h: commodity avg `0.0593` n `12`; crypto_alt avg `0.2548` n `234`; crypto_major avg `-0.1089` n `8`; equity avg `0.0549` n `141`; fx avg `0.0075` n `6`; index avg `0.0164` n `26`; metal avg `-0.0138` n `20`; unknown avg `-0.1145` n `949`
- 24h: commodity avg `0.0293` n `12`; crypto_alt avg `0.8938` n `234`; crypto_major avg `-0.2871` n `8`; equity avg `0.2266` n `141`; fx avg `0.0286` n `6`; index avg `0.0027` n `26`; metal avg `-0.0165` n `20`; unknown avg `4.4766` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
