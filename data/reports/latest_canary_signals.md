# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T18:07:28.052103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.2164` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.7693` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.7237` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0217` n `12`; crypto_alt avg `-0.0716` n `228`; crypto_major avg `-0.0366` n `8`; equity avg `-0.0082` n `78`; fx avg `-0.0375` n `6`; index avg `0.0126` n `23`; metal avg `0.0002` n `18`; unknown avg `-0.0583` n `687`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.3692` n `228`; crypto_major avg `0.4281` n `8`; equity avg `0.0474` n `78`; fx avg `-0.0087` n `6`; index avg `0.0043` n `23`; metal avg `0.0225` n `18`; unknown avg `-0.0143` n `687`
- 4h: commodity avg `0.2727` n `12`; crypto_alt avg `-3.304` n `228`; crypto_major avg `-4.4966` n `8`; equity avg `0.7198` n `78`; fx avg `-0.1046` n `6`; index avg `0.2271` n `23`; metal avg `-4.2493` n `18`; unknown avg `-0.356` n `572`
- 24h: commodity avg `0.2727` n `12`; crypto_alt avg `-3.304` n `228`; crypto_major avg `-4.4966` n `8`; equity avg `0.7198` n `78`; fx avg `-0.1046` n `6`; index avg `0.2271` n `23`; metal avg `-4.2493` n `18`; unknown avg `-0.356` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
