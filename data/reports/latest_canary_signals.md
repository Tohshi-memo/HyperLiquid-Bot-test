# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T10:07:27.171937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `0.1558` n `233`; crypto_major avg `0.1587` n `8`; equity avg `0.024` n `134`; fx avg `0.0163` n `6`; index avg `0.0029` n `26`; metal avg `-0.035` n `20`; unknown avg `0.0579` n `795`
- 1h: commodity avg `0.0764` n `12`; crypto_alt avg `-0.2032` n `233`; crypto_major avg `-0.1586` n `8`; equity avg `-0.0818` n `134`; fx avg `0.0173` n `6`; index avg `-0.0168` n `26`; metal avg `-0.0488` n `20`; unknown avg `0.7565` n `795`
- 4h: commodity avg `0.3019` n `12`; crypto_alt avg `-0.795` n `233`; crypto_major avg `-0.5269` n `8`; equity avg `-0.4153` n `134`; fx avg `0.0662` n `6`; index avg `-0.0776` n `26`; metal avg `-0.3102` n `20`; unknown avg `-0.2295` n `787`
- 24h: commodity avg `0.0126` n `12`; crypto_alt avg `-4.094` n `233`; crypto_major avg `-2.6036` n `8`; equity avg `-0.7346` n `134`; fx avg `0.1055` n `6`; index avg `-0.029` n `26`; metal avg `0.0881` n `20`; unknown avg `-1.0122` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
