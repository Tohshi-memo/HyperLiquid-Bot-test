# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T03:37:27.206108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0476` n `13`; crypto_alt avg `-0.1296` n `237`; crypto_major avg `-0.0827` n `8`; equity avg `0.0747` n `152`; fx avg `-0.0059` n `6`; index avg `0.0299` n `26`; metal avg `-0.0285` n `20`; unknown avg `2.8607` n `1240`
- 1h: commodity avg `-0.0842` n `13`; crypto_alt avg `-0.0035` n `237`; crypto_major avg `0.0175` n `8`; equity avg `0.224` n `152`; fx avg `0.0039` n `6`; index avg `0.0469` n `26`; metal avg `0.1622` n `20`; unknown avg `2.9677` n `1236`
- 4h: commodity avg `-0.289` n `13`; crypto_alt avg `-0.8477` n `237`; crypto_major avg `-0.7797` n `8`; equity avg `-0.9133` n `152`; fx avg `-0.0107` n `6`; index avg `-0.0778` n `26`; metal avg `0.0218` n `20`; unknown avg `4.6919` n `1162`
- 24h: commodity avg `-0.6867` n `13`; crypto_alt avg `-1.6578` n `237`; crypto_major avg `-1.4829` n `8`; equity avg `-0.7379` n `152`; fx avg `0.0404` n `6`; index avg `-0.0015` n `26`; metal avg `0.2088` n `20`; unknown avg `1.2111` n `987`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2451`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
