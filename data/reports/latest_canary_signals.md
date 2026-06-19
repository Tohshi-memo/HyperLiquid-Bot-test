# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T20:07:27.144231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.208` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.8058` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.7572` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0754` n `228`; crypto_major avg `0.0142` n `8`; equity avg `0.0093` n `78`; fx avg `0.0004` n `6`; index avg `0.0045` n `23`; metal avg `0.0531` n `18`; unknown avg `-0.0219` n `687`
- 1h: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.0651` n `228`; crypto_major avg `0.0074` n `8`; equity avg `-0.003` n `78`; fx avg `-0.0159` n `6`; index avg `0.0004` n `23`; metal avg `0.0908` n `18`; unknown avg `-0.2866` n `687`
- 4h: commodity avg `0.2745` n `12`; crypto_alt avg `-3.7392` n `228`; crypto_major avg `-4.5313` n `8`; equity avg `0.6767` n `78`; fx avg `-0.0922` n `6`; index avg `0.2259` n `23`; metal avg `-4.1594` n `18`; unknown avg `-0.4251` n `572`
- 24h: commodity avg `0.2745` n `12`; crypto_alt avg `-3.7392` n `228`; crypto_major avg `-4.5313` n `8`; equity avg `0.6767` n `78`; fx avg `-0.0922` n `6`; index avg `0.2259` n `23`; metal avg `-4.1594` n `18`; unknown avg `-0.4251` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
