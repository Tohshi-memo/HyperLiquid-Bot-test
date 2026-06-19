# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T16:22:31.022660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-5.2345` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-5.2345` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `-4.8058` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-4.8058` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `4.6335` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `4.6335` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.4412` n `12`; crypto_alt avg `-3.1921` n `228`; crypto_major avg `-4.3646` n `8`; equity avg `0.8699` n `78`; fx avg `-0.1087` n `6`; index avg `0.2689` n `23`; metal avg `-4.4215` n `18`; unknown avg `-0.3841` n `572`
- 1h: commodity avg `0.4412` n `12`; crypto_alt avg `-3.1921` n `228`; crypto_major avg `-4.3646` n `8`; equity avg `0.8699` n `78`; fx avg `-0.1087` n `6`; index avg `0.2689` n `23`; metal avg `-4.4215` n `18`; unknown avg `-0.3841` n `572`
- 4h: commodity avg `0.4412` n `12`; crypto_alt avg `-3.1921` n `228`; crypto_major avg `-4.3646` n `8`; equity avg `0.8699` n `78`; fx avg `-0.1087` n `6`; index avg `0.2689` n `23`; metal avg `-4.4215` n `18`; unknown avg `-0.3841` n `572`
- 24h: commodity avg `0.4412` n `12`; crypto_alt avg `-3.1921` n `228`; crypto_major avg `-4.3646` n `8`; equity avg `0.8699` n `78`; fx avg `-0.1087` n `6`; index avg `0.2689` n `23`; metal avg `-4.4215` n `18`; unknown avg `-0.3841` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0721`, n `671`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0682`, n `671`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `671`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0624`, n `671`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `671`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0597`, n `671`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0541`, n `671`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0524`, n `671`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0508`, n `671`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0496`, n `671`, weak_sample_signal
