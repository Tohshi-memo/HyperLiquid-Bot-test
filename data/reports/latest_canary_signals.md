# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T05:22:26.665366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3965` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0286` n `12`; crypto_alt avg `-0.4803` n `234`; crypto_major avg `-0.3362` n `8`; equity avg `-0.1778` n `141`; fx avg `0.0195` n `6`; index avg `-0.0288` n `26`; metal avg `-0.0553` n `20`; unknown avg `-0.1988` n `962`
- 1h: commodity avg `0.0868` n `12`; crypto_alt avg `-0.8109` n `234`; crypto_major avg `-0.4908` n `8`; equity avg `-0.2303` n `141`; fx avg `0.0508` n `6`; index avg `-0.0284` n `26`; metal avg `-0.1085` n `20`; unknown avg `24.8817` n `960`
- 4h: commodity avg `0.1569` n `12`; crypto_alt avg `-2.4169` n `234`; crypto_major avg `-1.4629` n `8`; equity avg `-0.8792` n `141`; fx avg `0.0141` n `6`; index avg `-0.0664` n `26`; metal avg `-0.2447` n `20`; unknown avg `228.1746` n `936`
- 24h: commodity avg `-0.2975` n `12`; crypto_alt avg `-1.9264` n `234`; crypto_major avg `-1.6024` n `8`; equity avg `-1.5706` n `141`; fx avg `0.0767` n `6`; index avg `-0.1645` n `26`; metal avg `-0.7804` n `20`; unknown avg `5.6616` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
