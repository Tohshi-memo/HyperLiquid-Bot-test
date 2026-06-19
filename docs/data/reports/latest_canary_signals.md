# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T17:37:33.532316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.3206` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `4.8391` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-4.8289` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `0.2742` n `228`; crypto_major avg `0.2849` n `8`; equity avg `0.0375` n `78`; fx avg `-0.0013` n `6`; index avg `0.0209` n `23`; metal avg `0.004` n `18`; unknown avg `0.0264` n `687`
- 1h: commodity avg `-0.1334` n `12`; crypto_alt avg `-0.1691` n `228`; crypto_major avg `-0.2028` n `8`; equity avg `-0.1059` n `78`; fx avg `0.027` n `6`; index avg `-0.0242` n `23`; metal avg `0.1562` n `18`; unknown avg `0.0097` n `687`
- 4h: commodity avg `0.2404` n `12`; crypto_alt avg `-3.3443` n `228`; crypto_major avg `-4.5885` n `8`; equity avg `0.7321` n `78`; fx avg `-0.0948` n `6`; index avg `0.2506` n `23`; metal avg `-4.2522` n `18`; unknown avg `-0.3667` n `572`
- 24h: commodity avg `0.2404` n `12`; crypto_alt avg `-3.3443` n `228`; crypto_major avg `-4.5885` n `8`; equity avg `0.7321` n `78`; fx avg `-0.0948` n `6`; index avg `0.2506` n `23`; metal avg `-4.2522` n `18`; unknown avg `-0.3667` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
