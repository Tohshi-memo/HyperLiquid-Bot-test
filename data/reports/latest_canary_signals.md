# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T17:52:31.236728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4299` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3519` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3385` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1078` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.044` n `12`; crypto_alt avg `-0.3838` n `234`; crypto_major avg `-0.1991` n `8`; equity avg `-0.1186` n `142`; fx avg `0.0057` n `6`; index avg `-0.0103` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.0941` n `962`
- 1h: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.6528` n `234`; crypto_major avg `-0.2228` n `8`; equity avg `-0.0918` n `142`; fx avg `0.0014` n `6`; index avg `0.0072` n `26`; metal avg `0.0104` n `20`; unknown avg `-0.2767` n `960`
- 4h: commodity avg `0.0135` n `12`; crypto_alt avg `-2.6266` n `234`; crypto_major avg `-2.4164` n `8`; equity avg `-0.3086` n `142`; fx avg `-0.0544` n `6`; index avg `-0.0645` n `26`; metal avg `-0.0779` n `20`; unknown avg `228.5179` n `892`
- 24h: commodity avg `-0.4492` n `12`; crypto_alt avg `-0.9408` n `234`; crypto_major avg `-1.6574` n `8`; equity avg `0.089` n `142`; fx avg `-0.1843` n `6`; index avg `-0.0748` n `26`; metal avg `-0.2229` n `20`; unknown avg `0.2861` n `786`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
