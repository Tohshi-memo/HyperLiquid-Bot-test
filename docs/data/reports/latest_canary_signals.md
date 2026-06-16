# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T13:52:40.697918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.08` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0413` n `12`; crypto_alt avg `0.0527` n `228`; crypto_major avg `-0.1799` n `8`; equity avg `0.3316` n `77`; fx avg `-0.0178` n `6`; index avg `0.0564` n `23`; metal avg `-0.0332` n `18`; unknown avg `0.0943` n `687`
- 1h: commodity avg `0.4836` n `12`; crypto_alt avg `-0.6898` n `228`; crypto_major avg `-0.8784` n `8`; equity avg `0.5159` n `77`; fx avg `-0.0004` n `6`; index avg `0.2016` n `23`; metal avg `-0.1633` n `18`; unknown avg `0.1827` n `687`
- 4h: commodity avg `-0.1184` n `12`; crypto_alt avg `-0.6032` n `228`; crypto_major avg `-0.3407` n `8`; equity avg `0.0298` n `77`; fx avg `-0.0183` n `6`; index avg `0.1636` n `23`; metal avg `0.1264` n `18`; unknown avg `0.6546` n `687`
- 24h: commodity avg `-0.0899` n `12`; crypto_alt avg `-1.4295` n `228`; crypto_major avg `0.3946` n `8`; equity avg `1.1848` n `77`; fx avg `-0.097` n `6`; index avg `0.1371` n `23`; metal avg `-0.1521` n `18`; unknown avg `0.4625` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
