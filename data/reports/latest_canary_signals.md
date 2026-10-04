# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T03:22:34.242343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `13`; crypto_alt avg `0.1675` n `235`; crypto_major avg `0.0545` n `8`; equity avg `-0.0014` n `143`; fx avg `-0.0015` n `6`; index avg `0.0011` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.0452` n `1079`
- 1h: commodity avg `-0.0574` n `13`; crypto_alt avg `0.2366` n `235`; crypto_major avg `0.0257` n `8`; equity avg `0.0121` n `143`; fx avg `-0.0033` n `6`; index avg `0.0009` n `26`; metal avg `0.0074` n `20`; unknown avg `-0.1751` n `1077`
- 4h: commodity avg `-0.064` n `13`; crypto_alt avg `-0.0541` n `235`; crypto_major avg `0.0496` n `8`; equity avg `-0.0265` n `143`; fx avg `-0.0023` n `6`; index avg `-0.0072` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.1843` n `1071`
- 24h: commodity avg `0.1017` n `13`; crypto_alt avg `1.2607` n `235`; crypto_major avg `0.6647` n `8`; equity avg `0.1748` n `143`; fx avg `-0.028` n `6`; index avg `0.0091` n `26`; metal avg `0.0086` n `20`; unknown avg `0.0942` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
