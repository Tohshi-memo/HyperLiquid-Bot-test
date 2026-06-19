# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T19:52:31.289914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.2122` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.8188` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.7664` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0263` n `12`; crypto_alt avg `0.2352` n `228`; crypto_major avg `0.1963` n `8`; equity avg `0.0177` n `78`; fx avg `0.043` n `6`; index avg `-0.0078` n `23`; metal avg `0.0103` n `18`; unknown avg `-0.2427` n `687`
- 1h: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.2541` n `228`; crypto_major avg `0.0135` n `8`; equity avg `-0.0172` n `78`; fx avg `0.0048` n `6`; index avg `0.0117` n `23`; metal avg `0.0373` n `18`; unknown avg `-0.3456` n `687`
- 4h: commodity avg `0.2741` n `12`; crypto_alt avg `-3.8118` n `228`; crypto_major avg `-4.5447` n `8`; equity avg `0.6675` n `78`; fx avg `-0.0925` n `6`; index avg `0.2217` n `23`; metal avg `-4.2094` n `18`; unknown avg `-0.4332` n `572`
- 24h: commodity avg `0.2741` n `12`; crypto_alt avg `-3.8118` n `228`; crypto_major avg `-4.5447` n `8`; equity avg `0.6675` n `78`; fx avg `-0.0925` n `6`; index avg `0.2217` n `23`; metal avg `-4.2094` n `18`; unknown avg `-0.4332` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
