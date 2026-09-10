# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T02:37:24.916810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `0.4431` n `233`; crypto_major avg `0.2603` n `8`; equity avg `0.0587` n `134`; fx avg `0.0047` n `6`; index avg `0.014` n `26`; metal avg `0.0289` n `20`; unknown avg `0.2132` n `797`
- 1h: commodity avg `-0.0898` n `12`; crypto_alt avg `0.405` n `233`; crypto_major avg `0.4934` n `8`; equity avg `0.2246` n `134`; fx avg `-0.0212` n `6`; index avg `0.0765` n `26`; metal avg `0.0762` n `20`; unknown avg `0.062` n `795`
- 4h: commodity avg `-0.1669` n `12`; crypto_alt avg `-0.0235` n `233`; crypto_major avg `0.1852` n `8`; equity avg `-0.3348` n `134`; fx avg `0.0045` n `6`; index avg `-0.0127` n `26`; metal avg `0.0376` n `20`; unknown avg `-0.0433` n `789`
- 24h: commodity avg `-0.0429` n `12`; crypto_alt avg `-3.2347` n `233`; crypto_major avg `-2.2016` n `8`; equity avg `-1.4662` n `134`; fx avg `-0.0383` n `6`; index avg `-0.2483` n `26`; metal avg `0.4989` n `20`; unknown avg `0.9331` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
