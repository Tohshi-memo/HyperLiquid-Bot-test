# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T02:52:28.172257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0666` n `12`; crypto_alt avg `0.0544` n `234`; crypto_major avg `0.0546` n `8`; equity avg `0.0937` n `137`; fx avg `-0.0165` n `6`; index avg `0.015` n `27`; metal avg `-0.0067` n `20`; unknown avg `0.1555` n `920`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `-0.0748` n `234`; crypto_major avg `-0.0767` n `8`; equity avg `0.1195` n `137`; fx avg `-0.0347` n `6`; index avg `0.007` n `27`; metal avg `-0.1017` n `20`; unknown avg `0.0873` n `917`
- 4h: commodity avg `0.0631` n `12`; crypto_alt avg `1.8057` n `234`; crypto_major avg `1.2999` n `8`; equity avg `0.5159` n `137`; fx avg `0.0095` n `6`; index avg `0.0877` n `27`; metal avg `0.1932` n `20`; unknown avg `1.2123` n `901`
- 24h: commodity avg `-0.4252` n `12`; crypto_alt avg `2.0093` n `234`; crypto_major avg `1.2204` n `8`; equity avg `1.438` n `137`; fx avg `0.0118` n `6`; index avg `0.1334` n `27`; metal avg `-0.2569` n `20`; unknown avg `0.9893` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
