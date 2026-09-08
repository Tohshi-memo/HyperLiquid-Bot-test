# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T15:52:26.168081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0772` n `12`; crypto_alt avg `0.2505` n `232`; crypto_major avg `0.3589` n `8`; equity avg `0.1095` n `134`; fx avg `0.0063` n `6`; index avg `0.0078` n `26`; metal avg `-0.0224` n `20`; unknown avg `-0.0873` n `797`
- 1h: commodity avg `-0.1047` n `12`; crypto_alt avg `0.6594` n `232`; crypto_major avg `0.5517` n `8`; equity avg `0.5067` n `134`; fx avg `0.0005` n `6`; index avg `0.0409` n `26`; metal avg `0.0165` n `20`; unknown avg `1.2523` n `795`
- 4h: commodity avg `-0.5997` n `12`; crypto_alt avg `1.0691` n `232`; crypto_major avg `0.9769` n `8`; equity avg `1.2862` n `134`; fx avg `0.0051` n `6`; index avg `0.0661` n `26`; metal avg `-0.018` n `20`; unknown avg `-0.0825` n `775`
- 24h: commodity avg `-0.2844` n `12`; crypto_alt avg `1.8278` n `232`; crypto_major avg `0.9297` n `8`; equity avg `1.2525` n `134`; fx avg `-0.0682` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0501` n `20`; unknown avg `7062.3574` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
