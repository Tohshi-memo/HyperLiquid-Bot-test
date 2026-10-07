# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T10:22:33.630391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `13`; crypto_alt avg `0.3813` n `235`; crypto_major avg `0.367` n `8`; equity avg `0.0097` n `150`; fx avg `-0.005` n `6`; index avg `-0.02` n `26`; metal avg `-0.0228` n `20`; unknown avg `3.2202` n `1076`
- 1h: commodity avg `0.0634` n `13`; crypto_alt avg `-0.185` n `235`; crypto_major avg `-0.1865` n `8`; equity avg `-0.0171` n `150`; fx avg `-0.0221` n `6`; index avg `-0.0278` n `26`; metal avg `-0.0392` n `20`; unknown avg `2.1217` n `1074`
- 4h: commodity avg `0.0629` n `13`; crypto_alt avg `-0.7542` n `235`; crypto_major avg `-0.5983` n `8`; equity avg `-0.6201` n `150`; fx avg `-0.115` n `6`; index avg `-0.1001` n `26`; metal avg `-0.246` n `20`; unknown avg `1.1651` n `1058`
- 24h: commodity avg `1.21` n `13`; crypto_alt avg `-4.5165` n `235`; crypto_major avg `-2.9942` n `8`; equity avg `-1.0655` n `150`; fx avg `-0.1034` n `6`; index avg `-0.222` n `26`; metal avg `-0.4377` n `20`; unknown avg `815.188` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
