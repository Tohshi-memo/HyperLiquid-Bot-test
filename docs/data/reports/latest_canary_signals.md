# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T18:37:30.322704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.2826` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.8827` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.8064` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.042` n `12`; crypto_alt avg `-0.2523` n `228`; crypto_major avg `-0.1684` n `8`; equity avg `-0.0218` n `78`; fx avg `0.019` n `6`; index avg `-0.0072` n `23`; metal avg `0.0282` n `18`; unknown avg `0.0375` n `687`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `-0.2617` n `228`; crypto_major avg `0.0005` n `8`; equity avg `-0.0319` n `78`; fx avg `0.0234` n `6`; index avg `-0.0275` n `23`; metal avg `0.0093` n `18`; unknown avg `0.0493` n `687`
- 4h: commodity avg `0.2976` n `12`; crypto_alt avg `-3.5981` n `228`; crypto_major avg `-4.5851` n `8`; equity avg `0.6975` n `78`; fx avg `-0.0715` n `6`; index avg `0.2213` n `23`; metal avg `-4.2434` n `18`; unknown avg `-0.3144` n `572`
- 24h: commodity avg `0.2976` n `12`; crypto_alt avg `-3.5981` n `228`; crypto_major avg `-4.5851` n `8`; equity avg `0.6975` n `78`; fx avg `-0.0715` n `6`; index avg `0.2213` n `23`; metal avg `-4.2434` n `18`; unknown avg `-0.3144` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
