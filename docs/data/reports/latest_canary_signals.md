# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T14:07:13.595474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0321` n `12`; crypto_alt avg `-0.1514` n `228`; crypto_major avg `-0.0172` n `8`; equity avg `-0.0436` n `65`; fx avg `0.0181` n `5`; index avg `0.0073` n `23`; metal avg `0.0058` n `18`; unknown avg `-0.1456` n `376`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.4442` n `228`; crypto_major avg `-0.1165` n `8`; equity avg `-0.039` n `65`; fx avg `0.0053` n `5`; index avg `0.0119` n `23`; metal avg `-0.012` n `18`; unknown avg `-0.3323` n `376`
- 4h: commodity avg `0.0788` n `12`; crypto_alt avg `-0.2554` n `228`; crypto_major avg `-0.0379` n `8`; equity avg `0.0383` n `65`; fx avg `0.0017` n `5`; index avg `0.0279` n `23`; metal avg `-0.0165` n `18`; unknown avg `-0.4706` n `376`
- 24h: commodity avg `-0.1664` n `12`; crypto_alt avg `2.4883` n `228`; crypto_major avg `1.917` n `8`; equity avg `1.8337` n `65`; fx avg `0.0207` n `5`; index avg `0.6422` n `23`; metal avg `-0.1244` n `18`; unknown avg `0.1819` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
