# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T04:07:35.524105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0671` n `12`; crypto_alt avg `0.333` n `233`; crypto_major avg `0.2074` n `8`; equity avg `0.0551` n `136`; fx avg `-0.0155` n `6`; index avg `0.017` n `26`; metal avg `0.0631` n `20`; unknown avg `0.1522` n `794`
- 1h: commodity avg `-0.0259` n `12`; crypto_alt avg `0.6626` n `233`; crypto_major avg `0.3899` n `8`; equity avg `-0.0257` n `136`; fx avg `-0.0273` n `6`; index avg `0.0182` n `26`; metal avg `0.0014` n `20`; unknown avg `2.3701` n `792`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.3369` n `233`; crypto_major avg `0.2295` n `8`; equity avg `-0.2166` n `136`; fx avg `-0.0559` n `6`; index avg `0.021` n `26`; metal avg `-0.0674` n `20`; unknown avg `-0.6245` n `780`
- 24h: commodity avg `1.1649` n `12`; crypto_alt avg `-1.9991` n `233`; crypto_major avg `-2.3951` n `8`; equity avg `-2.1345` n `136`; fx avg `0.0795` n `6`; index avg `-0.3522` n `26`; metal avg `-1.343` n `20`; unknown avg `-0.9734` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
