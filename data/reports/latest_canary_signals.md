# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T05:07:31.436266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0489` n `13`; crypto_alt avg `0.2419` n `235`; crypto_major avg `0.0453` n `8`; equity avg `0.0695` n `144`; fx avg `0.0058` n `6`; index avg `0.0081` n `26`; metal avg `0.0213` n `20`; unknown avg `-0.0719` n `1077`
- 1h: commodity avg `0.0267` n `13`; crypto_alt avg `-0.0655` n `235`; crypto_major avg `-0.1805` n `8`; equity avg `-0.0058` n `144`; fx avg `0.0529` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0347` n `20`; unknown avg `0.852` n `1065`
- 4h: commodity avg `-0.0942` n `13`; crypto_alt avg `-0.7212` n `235`; crypto_major avg `-0.7164` n `8`; equity avg `-0.303` n `144`; fx avg `0.0088` n `6`; index avg `-0.0874` n `26`; metal avg `-0.1673` n `20`; unknown avg `1.3557` n `982`
- 24h: commodity avg `-0.3279` n `13`; crypto_alt avg `0.2288` n `235`; crypto_major avg `0.7957` n `8`; equity avg `0.2506` n `144`; fx avg `-0.0665` n `6`; index avg `-0.0516` n `26`; metal avg `0.0466` n `20`; unknown avg `0.0518` n `904`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
