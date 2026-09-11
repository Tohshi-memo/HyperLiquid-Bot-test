# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T06:37:29.294697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0381` n `12`; crypto_alt avg `-0.2095` n `233`; crypto_major avg `-0.117` n `8`; equity avg `-0.0331` n `136`; fx avg `0.0163` n `6`; index avg `0.0123` n `26`; metal avg `-0.0295` n `20`; unknown avg `0.4836` n `796`
- 1h: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.0946` n `233`; crypto_major avg `0.0059` n `8`; equity avg `0.3059` n `136`; fx avg `0.0109` n `6`; index avg `0.0733` n `26`; metal avg `0.0823` n `20`; unknown avg `0.4108` n `772`
- 4h: commodity avg `-0.2749` n `12`; crypto_alt avg `0.6487` n `233`; crypto_major avg `0.5503` n `8`; equity avg `0.6031` n `136`; fx avg `-0.0211` n `6`; index avg `0.1666` n `26`; metal avg `0.3566` n `20`; unknown avg `27.0212` n `764`
- 24h: commodity avg `0.9555` n `12`; crypto_alt avg `-1.4981` n `233`; crypto_major avg `-1.6385` n `8`; equity avg `-1.5337` n `136`; fx avg `0.0842` n `6`; index avg `-0.2666` n `26`; metal avg `-1.0284` n `20`; unknown avg `1.1619` n `685`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
